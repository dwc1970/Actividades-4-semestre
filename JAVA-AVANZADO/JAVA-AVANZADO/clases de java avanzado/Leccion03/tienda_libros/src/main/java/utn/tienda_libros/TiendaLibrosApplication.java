package utn.tienda_libros;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.tienda_libros.vista.LibroFrom;

import java.awt.*;

@SpringBootApplication
public class TiendaLibrosApplication {

	public static void main(String[] args) {

		ConfigurableApplicarionContext = contextoSpring
		new SpringApplicationBuilder(TiendaLibrosApplication.class)
				.headless(false)
				.web(WebApplicationType.NONE)
				.run(args);

		// Ejecutamos el codigo para cargar el formulario
		EventQueue.invokeLater(() - > {
				//Obtenemos el ojeto from a través del spring
				LibroFrom librosFrom = contextoSpring(LibroFrom.class);
		librosFrom.setVisible(true);
	    });
	}
}
