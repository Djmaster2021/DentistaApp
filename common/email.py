def enviar_correo_confirmacion(cita, paciente):
    print("📧 Enviando correo de confirmación...")
    print(f"Para: {paciente.get('correo')}")
    print(f"Nombre: {paciente.get('nombre')}")
    print(f"Servicio: {cita.get('servicio')}")
    print("✅ Correo enviado.")


def enviar_factura(cita, paciente, pago):
    print("📧 Enviando factura al correo electrónico...")
    print(f"Para: {paciente.get('correo')}")
    print(f"Nombre: {paciente.get('nombre')}")
    print(f"Servicio: {cita.get('servicio')}")
    print(f"Tarjeta terminación: ****{pago.get('numero', '')[-4:]}")
    print("✅ Factura enviada.")
