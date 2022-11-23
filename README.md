# Final-Project-Coderhouse
Final project for Codehouse Python course: Rodriguez Canovari Santiago, Tomas Ignacio Oldenburg.

Funcionalidades y paths:

    Registro de usuarios: /AppFinalProject/signup/
    Autenticacion de usuario: /AppFinalProject/login
    Cerrar sesion: /AppFinalProject/logout
    Listado de posteos:  /AppFinalProject/Posts
    Listado de escritores: /AppFinalProject/writters
    Creación de posts(Solo escritores): /AppFinalProject/%5Enew$
    Borrar posts(Solo Admins): /AppFinalProject/%5Edelete/(?P<pk>\d+)$
    Perfil del usuario logueado: /AppFinalProject/%5Eprofile/$
    Edicion de usuario: /AppFinalProject/%5Eprofile/edit/$
    Cambiar contraseña: /AppFinalProject/%5Eprofile/edit/password/$
    FeedBack de cambio de contraseña exitoso: /AppFinalProject/%5Eprofile/edit/password_success/$
    Creación de grupos (Solo desde admin django): /admin
	
    
Tambien se pueden apreciar las distintas vistas donde serán implementadas dichas funcionalidades en el path:/AppFinalProject/home/

Todas las vistas requieren que el usuario este registrado y logueado para ser accedidas.

Cada uno está implementado con un form en la URL indicado.

Se adjunta una DB ya creada con datos de prueba para que pueda ser probado de manera más comoda.
