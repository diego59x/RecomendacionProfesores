import java.util.*;
import java.io.*;
public class Vista {



	ArrayList<String> respuestas = new ArrayList<String>();
	Scanner scan = new Scanner(System.in);
	public ArrayList<String> preguntas(){
		
		System.out.println("+\t\t1. ¿Cual de las siguientes actividades disfrutas mas?\t\t \n+\t\t 1. Escuchar musica\t\t \n+\t\t 2. Ver peliculas \t\t\n+\t\t 3. Bailar con buena musica\t\t");
		respuestas.add(scan.nextLine());
		System.out.println("+\t\t2. Cuando conversas con otra persona, tu \n+\t\t 1. La escuchas atentamente \n+\t\t 2. La observas \n+\t\t 3. Tiendes a tocarla");
		respuestas.add(scan.nextLine());
		System.out.println("+\t\t3. ¿Que tipo de examenes se te facilitan mas? \n+\t\t 1. Examen oral \n+\t\t 2. Examen escrito \n+\t\t 3. Examen de opcion multiple");
		respuestas.add(scan.nextLine());
		System.out.println("+\t\t4. ¿Como te orientas mas facilmente? \n+\t\t 1. Mediante el uso de un mapa \n+\t\t 2. Pidiendo indicaciones \n+\t\t 3. A traves de la intuicion");
		respuestas.add(scan.nextLine());
		System.out.println("+\t\t5. ¿De que manera se te facilita aprender algo? \n+\t\t 1. Repitiendo en voz alta \n+\t\t 2. Escribieno varias veces \n+\t\t 3. Relacionandolo con algo divertido");
		respuestas.add(scan.nextLine());
		System.out.println("+\t\t6. ¿Cuando tratas de recordar algo, ¿Como lo haces? \n+\t\t 1. A traves de imagenes \n+\t\t 2. A traves de emociones \n+\t\t 3. A traves de sonidos");
		respuestas.add(scan.nextLine());
		System.out.println("+\t\t7. ¿Como se te facilia entender algo? \n+\t\t 1. Cuando te lo explican verbalmente \n+\t\t 2. Cuando utilizan medios visuales \n+\t\t 3. Cuando se realiza a traves de alguna actividad");
		respuestas.add(scan.nextLine());
		respuestas();
		return respuestas;
		}
	public void respuestas(){
		System.out.println("Tus respuestas fueron: ");
		for(int i = 0; i<respuestas.size(); i++){
			System.out.println("Para la pregunta " + String.valueOf(i+1) + " respondiste: "  + respuestas.get(i));
		}
	}

}
