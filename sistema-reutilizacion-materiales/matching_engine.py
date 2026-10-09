import os
from supabase import create_client, Client

# Configuración de credenciales Supabase
SUPABASE_URL = "https://gfbcpnihwfndtkstoakv.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "TU_SECRET_KEY_AQUI")

def ejecutar_matching_engine():
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Conexión establecida con Supabase via API REST.\n")

        # Consultar inventario disponible y necesidades pendientes
        scrap_data = supabase.table("inventario_scrap").select("*, plantas(nombre)").eq("estado", "Disponible").execute()
        necesidades_data = supabase.table("necesidades_material").select("*, plantas(nombre)").eq("estado", "Pendiente").execute()

        coincidencias = []

        # Algoritmo de cruce
        for scrap in scrap_data.data:
            for nec in necesidades_data.data:
                if (
                    scrap["tipo_material"] == nec["tipo_material"] and
                    scrap["calibre"] == nec["calibre"] and
                    float(scrap["largo_mm"]) >= float(nec["largo_max_mm"]) and
                    float(scrap["ancho_mm"]) >= float(nec["ancho_max_mm"]) and
                    scrap["planta_origen_id"] != nec["planta_solicitante_id"]
                ):
                    coincidencias.append({
                        "material_id": scrap["material_id"],
                        "planta_ofrece": scrap["plantas"]["nombre"],
                        "planta_necesita": nec["plantas"]["nombre"],
                        "tipo_material": scrap["tipo_material"],
                        "calibre": scrap["calibre"],
                        "largo": scrap["largo_mm"],
                        "ancho": scrap["ancho_mm"],
                        "cantidad": scrap["cantidad"]
                    })

        # Mostrar resultados
        if coincidencias:
            print(f"🎯 SE ENCONTRARON {len(coincidencias)} COINCIDENCIA(S) DE REUTILIZACIÓN:\n")
            for match in coincidencias:
                print(f"📌 Material ID: {match['material_id']}")
                print(f"   • Se genera en: {match['planta_ofrece']}")
                print(f"   • Requerido por: {match['planta_necesita']}")
                print(f"   • Especificación: {match['tipo_material']} ({match['calibre']})")
                print(f"   • Medidas disponibles: {match['largo']}mm x {match['ancho']}mm | Cantidad: {match['cantidad']} unidades")
                print("-" * 50)
        else:
            print("⚠️ No hay coincidencias de material en este momento.")

    except Exception as e:
        print(f"❌ Error al consultar Supabase: {e}")

if __name__ == "__main__":
    ejecutar_matching_engine()
