package utn.tienda_libros.vista;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import utn.tienda_libros.Repositorio.LibroRepositorio;
import utn.tienda_libros.Servicio.LibroServicio;


import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

@Component
public class LibroFrom extends JFrame {
    LibroServicio libroServicio;
    private JTable TablaLibros;
    private DefaultTableModel tableModelLibros;

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

    private  void iniciarForma() {
        setContentPane(panel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        setSize(900, 700);
        // para obtener las demimenciones de la ventana
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension tamanioPantalla = toolkit.getSreenSize();
        int x = (tamanioPantalla.width - getWidth() / 2);
        int y = (tamanioPantalla.heigth - getHeight() / 2);
        setLocation(x, y);
    }
    private void createUIComponents() {
        this.tableModelLibros = new DefaultTableModel(0, 5);
        String[] cabecera = {"Id", "Libro", "Precio", "Existencias"};
        this.tableModelLibros.setColumnIdentifiers(cabecera);
        //Instanciar el objeto de Jtable
        this.tablaLibros = new JPanel(tableModeloLibros);
        listarLibros();
        }

        private  void listarLibros(){
            //Limpiar la tabla
            tableModeloLibros.setRowCount(0);
            //Obtener los libros de la BD
            var libros = LibroServicio.listarLibros();
            //Iteramos cada libro
            libros.forEach(libro) -> { // Funcion Lambda
                //Creamos cada registro para agregarlos a la tabla
                Object [] renglonLibro = {
                        libro.getIdLibro(),
                        libros.getNombreLibbro(),
                        libro.getAutor(),
                };
                this.tableModeloLibros.addRow(renglonLibro);
            });
    }
}
