import java.util.*;
import java.io.*;
public class Controlador {

	Vista vista = new Vista();
	ArrayList<String> respuestas = new ArrayList<String>();

	public void preguntas(){

		respuestas = vista.preguntas();
		
	}


}
