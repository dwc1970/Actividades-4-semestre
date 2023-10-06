package utn.tienda_libros.Servicio;

import utn.tienda_libros.modelo.Libro;

import java.util.List;

public interface IlibroServicio {

    public List<Libro> listarLibros();

    public Libro buscarLibroPorId(Integer IdLibro);

    public void guardarLibro(Libro libro);

    public void eliminarLibro( Libro libro);
}
