package utn.tienda_libros.Servicio;

import org.springframework.stereotype.Service;
import utn.tienda_libros.Repositorio.LibroRepositorio;

import java.util.List;

@Service
public class LibroServicio implements IlibroServicio {
    @Override
    public List<Libro> listarLibros() {
        return LibroRepositorio.findAll();
    }

    @Override
    public Libro buscarLibroPorId(Integer IdLibro) {
        Libro libro = libroRepositorio.findById(idLibro).orElse(null);
        return libro;
    }

    @Override
    public void guardarLibro(Libro libro) {
        libroRepositorio.save(libro);

    }

    @Override
    public void eliminarLibro(Libro libro) {
        libroRepositorio.delete(libro);

    }
}
