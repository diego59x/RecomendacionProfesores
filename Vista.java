import java.util.*;
import java.io.*;
public class Vista {



	ArrayList<String> respuestas = new ArrayList<String>();
	Scanner scan = new Scanner(System.in);
	int contador = 0;
	String preguntas = "\n";
	public ArrayList<String> preguntas(){
		File f = new File("Preguntas.txt");
	   	BufferedReader entrada;
	    try {
	           entrada = new BufferedReader(new FileReader(f));
	           while(entrada.ready()){
	                preguntas += entrada.readLine() + "\n";
	            }
	    }catch (IOException e) {
	            e.printStackTrace();
		}
		String[] partes = preguntas.split(",");
		for(int i = 1;i < partes.length; i++){
			
			System.out.println(partes[i-1]);
			if((i > 0 && i%4 == 0)){
				respuestas.add(scan.nextLine());
			}
		}
	
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
