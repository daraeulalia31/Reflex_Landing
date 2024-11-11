import reflex as rx
def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
        rx.color_mode.button(position="top-right"),
        
        rx.heading("Bienvenido Pc Store!", size="9",color="Red"),
        rx.hstack(
            rx.text(
                "Pc Store es una aplicación móvil diseñada para conectar a los amantes de las Pc con una alta tecnologia y opciones diferentes. Su nombre, Pc Store, Da a conocer los multiples tipos de pc , haciendo referencia a la calidad y precio de opciones que ofrece la aplicación",
                size="5", color="Red"
            ),
            rx.text( 
                """Pc Store es reconocidad por su calidad, precios y variedad de Pc .
Somos Computer Shop con más de 15 años de experiencia en Ventas de Equipos de cómputo de la línea Gamer, Laptops, Monitores, Placas Madre,componentes y 
precios justos"
 
""",
                size="5", color="Red"
            ),
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",color_scheme="Blue"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button("categoria",color_scheme="White"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="instagram"),color_scheme="White"),
                        href="https://instagram.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),color_scheme="blue"),
                        href="",
                        is_external=True,
                    ),
                ),
                rx.image(src="https://centrocomerciallaballena.com/wp-content/uploads/2024/05/IMG_7570.jpeg"),
                rx.image(src="https://lh5.googleusercontent.com/proxy/9Tb-iVp9C7PanjXVf8gUSUrFGkU5CecYCWffvRHBN7KD6vEyx9cirdQ15ncAAi2eGF5FMpD8mWoRa2cWYCdP9PsUosQrSdpB62wcPMkF0fIEC26R4A4GZfIg3VnZoupiQNfZng"),
                rx.image(src="https://s.yimg.com/ny/api/res/1.2/w.3a9oZ1c6iq0OgAWcmBMg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MA--/https://o.aolcdn.com/images/dar/5845cadfecd996e0372f/00903991c0317ca54a58a4c25779ac69a4d57787/aHR0cDovL28uYW9sY2RuLmNvbS9oc3Mvc3RvcmFnZS9taWRhcy9mZjRlZTI1M2M1ZGU0YTJhN2QyOGM3MWMwOGRkYmFkOS8yMDM3MjExMzQvY29tcHV0ZXIrc3RvcmUucG5n"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        bg="#661FF2"
    ),
app = rx.App()
app.add_page(index)