import time, logging
from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot(Token)
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=["start"])
def bot_mensajes_texto(message):
    print(message.from_user)
    bot.send_message(message.chat.id, "Hola " + str(message.from_user.first_name) + "," + " espero que estes muy bien" + " \U0001F600")
    bot.send_message(message.chat.id, """ Mi nombre es Javier bot, estoy programado para guiar y ayudar a las personas que inician en el mundo de la programacion \U0001F44C, pulsa sobre las siguentes opciones segun tus intereses o necesidades:  
    
/dudas

/canales_de_youtube

/ayuda
 
/desarrollador""")

@bot.message_handler(commands=["dudas"])
def cmd_dudas(message):
    bot.reply_to(message, "Perfecto, es hora de explorar las dudas y preguntas frecuentes que se hacen las personas antes de iniciar en la programacion" + " \U0001F603")
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="Pulsa sobre uno de estos botones")
    markup.add("1", "2", "3", row_width=1)
    bot.send_message(message.chat.id, """ Escoge una de estas opciones segun tus necesidades:
        
1- Porque aprender a programar

2- Ruta de aprendizaje

3- Areas en la programacion """, reply_markup=markup)

@bot.message_handler()
def keyboard_questions(message):
    if message.text == "1" or message.text == "Porque aprender a programar":
        markup = ReplyKeyboardRemove()
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(4)
        bot.send_message(message.chat.id, "Hasta el dia de hoy se han escrito miles de articulos con razones por las que debes aprender a programar, las razones son infinitas. Permiteme mencionarte algunas de estas razones de forma breve:", reply_markup=markup)

        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(6)
        bot.send_message(message.chat.id, "1- Has notado que dia a dia muchos procesos se repiten mecanicamente, Si una tarea implica tiempo y esfuerzo de humanos, entonces, debemos optimizar esa tarea, automatizandola, Como se logra eso? programando.")


        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(9)
        bot.send_message(message.chat.id, "2- Programar implica desarrollar algoritmos para resolver problemas de todo tipo. La inteligencia es la capacidad para resolver problemas. Por tanto, programar es una actividad que nos hace sentir vivos, y demuestra que somos seres inteligentes.")

    elif message.text == "2" or message.text == "Ruta de aprendizaje":
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Es importante que tengas bien en claro que es lo que quieres desarrollar en un inicio, recuerda que podras programar de todo. Pero debes empezar por una tecnologia en especifico. No te preocupes si no comprendes algunos terminos, porque iras aprendiendo nuevos conceptos en pocos segundos" + " \U0001F609", reply_markup=markup)

        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(7)
        bot.send_message(message.chat.id, "<b>Fundamentos de la programacion:</b>" + " Como declarar variables, como asignar valores, como realizar tareas repetitivas usando bucles, como hacer uso de condicionales, y mas conceptos generales.", parse_mode='HTML')
        bot.send_message(message.chat.id, "<b>Pseudocodigo y algoritmos:</b>" + " Estos ejercicios permiten desarrollar nuestra logica de programacion. Y esta fase sera muy determinante para las fases siguientes, ya que la base de todo es la practica y entender perfectamente lo que estas haciendo.", parse_mode='HTML')

        bot.send_message(message.chat.id, "Para que puedas entender mejor como funcionan los algoritmos en programacion, te invito a ver estos dos videos:" + "\n" + "\n"  + 'a href= "https://www.youtube.com/watch?v=sQLn2asTefo&t=128s/"><a/> ')
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(7)
        bot.send_message(message.chat.id, 'a href= "https://www.youtube.com/watch?v=SDv2vOIFIj8&t=189s/"></a>')


    elif message.text == "3" or message.text == "Areas en la programacion":
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "<b>Cuales son las areas de la programacion?</b>" +  " \U0001F914" + "\n" + "\n" + "La programacion es la carrera con mayor demanda y si eres programador nunca te vas a quedar sin trabajo. Pero en que industrias puedes trabajar como programador? te lo explicare para que escojas con sabiduria el camino a tomar.",parse_mode="HTML", reply_markup=markup)
        bot.send_message(message.chat.id, "A continuacion te presentare las areas en la programacion para que veas cual de ellos te llama mas la atencion y sepas en cual quieres especializarte" + " \U0001F60E" + "\n" + """ 
/Desarrollo_web

/Desarrollo_movil

/Desarrollo_de_videojuegos

/Aplicaciones_de_escritorio

/Sistemas_operativos

/Realidad_virtual_y_aumentada

/Maching_learning

/Cloud_computing
""")
    #Desarrollo web
    elif message.text == "/Desarrollo_web":
             bot.reply_to(message, "<b>1) Desarrollo web</b>" + "\n" + "\n" + "<b>Sitios web</b>: Son solo paginas web informativas. Su funcion es meramente informar al usuario, sea sobre un negocio, escuela, etc. Se puede utilizar un CMS como WordPress para crearlos." + "\n" + "\n" + " <b>Aplicaciones web</b>: Es una aplicacion completa y contiene una logica compleja, por ejemplo: YouTube es una aplicacion web, se pueden realizar funciones como guardar videos, crear una transmision, marcar favoritos, etc. Si te interesa saber cual es la ruta de aprendizaje de un desarrollador web por favor vea este video:" + "<a href = 'https://www.youtube.com/watch?v=rnmbxqS1nRo&t=49s/'></a>", parse_mode='html')
             bot.send_message(message.chat.id,
                              "<a href = 'https://www.youtube.com/watch?v=rnmbxqS1nRo&t=49s/'>Desarrollo web</a>",
                              parse_mode="HTML")

    #Desarrollo movil
    elif message.text == "/Desarrollo_movil":
        bot.reply_to(message,
                     "<b>Desarrollo movil</b>" + "\n" + "\n" + "El desarrollo movil es simples palabras es crear aplicaciones para telefonos y estas pueden funcionar en 2 sistemas operativos: Android de Google y iOS de Apple.",parse_mode='html')

        bot.send_message(message.chat.id,
                         "Si te interesa saber la ruta para aprender desarrollo movil vea estos 2 videos:" + "\n" + "<a href = 'https://www.youtube.com/watch?v=Jhqm9rkyrxQ/'>Desarrollo movil</a>",
                         parse_mode="HTML")
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(5)
        bot.send_message(message.chat.id, "<a href = 'https://www.youtube.com/watch?v=HYugxv0SqoM/'>Desarrollo movil</a>", parse_mode='HTML')

    # Desarrollo de videojuegos
    elif message.text == "/Desarrollo_de_videojuegos":
        bot.send_message(message.chat.id, "<b>Videojuegos</b>" + "\n" + "\n"+ "Ya todos los conocemos, tienen sus propias consolas, estan en moviles, en ordenadores y consolas. Su mundo es enorme, hay diseñadores, storytelling, modelado de personajes. Entre los motores mas importantes que puedes usar para desarrollar videojuegos se encuentran, Unity 3D que utiliza C# y Unreal Engine que usa C++", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(5)
        bot.send_message(message.chat.id, "Si te interesa saber mas sobre el desarrollo de videojuegos y la ruta de aprendizaje le invito a ver este video:" + "\n" + " <a href = 'https://www.youtube.com/watch?v=Jhqm9rkyrxQ/'>Desarrollo de videojuegos</a>", parse_mode='HTML')

    # Desktop apps
    elif message.text == "/Aplicaciones_de_escritorio":
        bot.send_message(message.chat.id,
                         "<b>Desktop Apps</b>" + "\n" + "\n" + "Son aplicaciones que se instalan directamente en tu sistema operativo de computadora sea Windows,Linux, Mac OS, por ejemplo: Adobe Premier, Office, un editor de codigo, un IDE. Para desarrollar este tipo de aplicaciones se pueden utilizar lenguajes como Java, C#, Python.", parse_mode='HTML')

    #Sistemas operativos
    elif message.text == "/Sistemas_operativos":
        bot.send_message(message.chat.id, "<b>Sistemas operativos o embebidos</b>" +
                         "\n" + "\n" + "Los sistemas operativos son justamente Windows, Linux, Android o IOS, es la capa mas baja de software que se comunica directamente con el hardware. Se suelen usar lenguajes como Ensamblador o C para desarrollarlos.", parse_mode='HTML')
        bot.send_message(message.chat.id, "Mientras que los <b>sistemas embebidos</b> son programas electronicos que realizan pocas funciones y estan hechos para cubrir necesidades especificas, casi siempre van directamente en un chip; por ejemplo: las operaciones de una lavadora, un refrigerador o algun otro electrodomestico.", parse_mode='HTML')

    #Maching learning
    elif message.text == "/Maching_learning":
        bot.send_message(message.chat.id, "<b>Maching learning</b>" + "\n" + "\n" + "Basicamente consiste en enseñarle a las computadores a traves de enormes volumenes de datos, el papel de los programadores en este ambito es crear los modelos, es decir la secuencia de pasos para que en Machine learning se pueda crear algo, y asi encontrar patrones para poder predecir una accion a futuro, por ejemplo: en Netflix los usuarios reciben recomendaciones en base a las peliculas/series que observaron previamente.", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(8)
        bot.send_message(message.chat.id, "De igual manera se podria hacer un analisis de sentimientos en marketing, para conocer que tan a gusto se sienten los usuarios con 'x' servicio, para asi poder fidelizarlos. Los 2 lenguajes mas importantes en el Machine learning son Python y R." + "\n" + "\n" + " <a href = 'https://www.youtube.com/watch?v=_OcLeySukXA/'>Maching Learning</a>", parse_mode='HTML')

    #Realidad virtual y aumentada
    elif message.text == "/Realidad_virtual_y_aumentada":
        bot.send_message(message.chat.id, "<b>Realidad virtual y Aumentada</b>" + "\n" + "\n" + "La realidad virtual es una inmersion total, se suele utilizar un casco o lentes que ocupa toda tu vision, y con ello puedes transportarte a un mundo virtual, hay proyectos muy conocidos como Beat Saber y Half-Life: Alyx.", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(7)
        bot.send_message(message.chat.id, "Mientras que la <b>realidad aumentada</b> combina nuestra realidad con la virtual, un ejemplo de ello es Pokemon GO o los filtros de Snapchat. y como funciona? Es muy simple, solo se necesita un dispositivo que permita observar el entorno, por ejemplo con la camara del telefono que puedes agregar efectos para las stories. Esta tecnologia se puede trabajar con varios lenguajes, tales como C#, Java, Javascript, Python, entre otros.", parse_mode='HTML')

    #Cloud computing
    elif message.text == "/Cloud_computing":
        bot.send_message(message.chat.id, "<b>Cloud computing</b>" + "\n" + "\n" + "La nube es una red mundial de servidores que ofrecen servicios de almacenamiento, bases de datos, redes, software, analisis e inteligencia a traves de internet. Esto les permite a las empresas y usuarios pagar solamente por lo que usan, lo cual realmente es un beneficio enorme. Ya que no tienen que adquirir equipos caros y todo lo que conllevan, sino que por un pago menor pueden optar hasta por una supercomputadora.", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(7)
        bot.send_message(message.chat.id, "Si le interesa saber mas sobre cloud computing le invito a ver este video:" + "\n" + "\n" + " <a href = 'https://www.youtube.com/watch?v=h4Af5bbFAq0/'>Cloud computing</a> ", parse_mode='HTML')

    elif message.text == "/ayuda":
        bot.reply_to(message, """Para que puedas comunicarte con este bot es importante que sepas algunas cosas importantes:

Si por alguna razon deseas regresar al menu de las areas en la programacion puedes escribir /volver

Si por alguna razon deseas salir puedes escribir "Salir" o pulsa el comando /salir

si desea volver a inicio escriba "inicio"

Tenga en cuenta que el bot no puede responderle mensajes al azar""")

    elif message.text == "/volver":
        bot.send_message(message.chat.id, """
/Desarrollo_web

/Desarrollo_movil

/Desarrollo_de_videojuegos

/Aplicaciones_de_escritorio

/Sistemas_operativos

/Realidad_virtual_y_aumentada

/Maching_learning

/Cloud_computing""")

    elif message.text == "/desarrollador":
        bot.reply_to(message, "Si usted desea hablar o saber quien me programo le dejare su contacto" + " \U0001F609")
        bot.send_contact(message.chat.id, phone_number="18498544377", first_name="pradelson", last_name="Francois")

    elif message.text == "Salir" or message.text == "salir" or message.text == "/salir":
        bot.send_message(message.chat.id, "Muchisimas Gracias por comunicarte conmigo, comparte mi contacto con otras personas y espero haberte ayudado con las dudas y preguntas, si tienes una meta... planifica, analiza, da lo mejor de ti y veras como se cumpliran" + " \U0001F609" + " \U0001F60C")

    elif message.text == "/canales_de_youtube":
        markup = InlineKeyboardMarkup(row_width=2)
        Btn1 = InlineKeyboardButton("Fatz", url="https://www.youtube.com/c/FaztTech")
        Btn2 = InlineKeyboardButton("UskoKrum2010", url="https://www.youtube.com/c/UskoKruM2010")
        Btn3 = InlineKeyboardButton("ProgramacionAts", url="https://www.youtube.com/c/Programaci%C3%B3nATS")
        Btn4 = InlineKeyboardButton("Programador x", url="https://www.youtube.com/c/ProgramadorX")
        Btn5 = InlineKeyboardButton("Soy dalto", url="https://www.youtube.com/c/soydalto")
        Btn6 = InlineKeyboardButton("LaGeekipediaDeErnesto", url="https://www.youtube.com/c/LaGeekipediaDeErnesto/videos")
        Btn7 = InlineKeyboardButton("Freecodecamp", url="https://www.youtube.com/c/Freecodecamp/videos")
        Btn8 = InlineKeyboardButton("Absolute", url="https://www.youtube.com/c/AbsoluteSite/videos")

        markup.add(Btn1, Btn2, Btn3, Btn4, Btn5, Btn6, Btn7, Btn8)
        bot.send_message(message.chat.id, "Si tienes conocimientos de programacion y necesitas canales de youtube populares sobre programacion aqui te lo dejo para que le des un ojo" +  " \U0001F44A", reply_markup=markup)

    elif message.text == "inicio" or message.text == "Inicio":
        bot.send_message(message.chat.id, """ Mi nombre es Javier, estoy programado para guiar y ayudar a las personas que inician en el mundo de la programacion ya que muchos estan bastante confundidos y no saben por donde empezar \U0001F44C, pulsa sobre las siguentes opciones segun tus intereses o necesidades:  
        
/dudas

/ayuda """)

    else:
        bot.reply_to(message, "Lo siento, no puedo responder ese mensaje" + " \U0001F609")

if __name__ == '__main__':
    print('iniciando el bot')
    bot.infinity_polling()