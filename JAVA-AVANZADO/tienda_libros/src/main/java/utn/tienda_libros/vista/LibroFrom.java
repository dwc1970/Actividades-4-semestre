package utn.tienda_libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import utn.tienda_libros.Repositorio.LibroRepositorio;
import utn.tienda_libros.Servicio.LibroServicio;


import javax.swing.*;

public class LibroFrom extends JFrame {
    LibroServicio libroServicio;

    @Autowired
    public LibroFrom(LibroRepositorio libroServicio){
        this.libroServicio = libroServicio;
        private JPanel panel;

         }
    @Autowired
    public LibroFrom(LibroServicio libroServicio){
        this.libroServicio = libroServicio;
        iniciarForma();
    }

    private  void iniciarForma(){
        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900, 700);
    }
}
