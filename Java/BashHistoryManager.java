import java.io.*;
public class BashHistoryManager {
    public static void main(String[] args) throws IOException{
	String in_filename, out_filename;
	if( args.length != 2 ){
	    System.out.println("USAGE:\njava BashHistoryManager {in_filename} {out_filename}\njava BashHistoryManager -in_place {filename}");
	    return;
	}
	final boolean in_place = args[0].equalsIgnoreCase("-in_place");
	if(in_place){
	    in_filename = out_filename = args[1];
	}
	else{
	    in_filename = args[0];
	    out_filename = args[1];
	}
	
	java.util.TreeMap<String, String> tree = read_file( in_filename );
	print_to_file( tree, out_filename );
	
    }
    
    private final static void print_to_file( java.util.TreeMap<String, String> tree, String filename ) throws IOException{
	
	BufferedWriter out = new BufferedWriter(new FileWriter(filename));
	for( String s : tree.keySet() ){
	    out.write( s + "\n" );
	}
	out.close();
    }
    
    public static java.util.TreeMap<String, String> read_file( String filename ) throws IOException{

	java.util.TreeMap<String, String> tree = new java.util.TreeMap<String, String>();
	
	BufferedReader in = new BufferedReader(new FileReader(filename));
	for(String line = in.readLine(); line != null; line=in.readLine()){
	    if( string_is_to_be_kept(line) && !tree.containsKey( line )){
		tree.put(line, line);
	    }
	}
	in.close();
	
	return tree;
    }
    
    final private static boolean string_is_to_be_kept( String cmd ){
	cmd = cmd.trim();
	if( cmd.contains(">") || cmd.contains("&&") )
	    return true;
	
	if( cmd.contains(";")){
	    String[] split = cmd.split(";");
	    for(String s : split){
		if( string_is_to_be_kept(s) ) return true;
	    }
	    return false;
	}
	
	if(cmd.startsWith("ls") || cmd.startsWith("exit") || cmd.startsWith("tmux") || cmd.startsWith("fg") || cmd.startsWith("cd") || cmd.startsWith("emacs") || cmd.startsWith("less")
	   || cmd.startsWith("rm") || cmd.startsWith("\rm") || cmd.startsWith("mv") || cmd.startsWith("cp") || cmd.startsWith("scp") || cmd.startsWith("git ") || cmd.startsWith("tar")
	   || cmd.startsWith("echo") || cmd.startsWith("cat") || cmd.startsWith("javac") || cmd.startsWith("mkdir") || cmd.startsWith("du -sh") || cmd.startsWith("chmod ")
	   || cmd.startsWith("wc ") || cmd.startsWith("tail") )
	    return false;
	
	//Wiggins
	if(cmd.startsWith("./scons.py") || cmd.startsWith("$emacs"))
	    return false;
	
	//KD
	if(cmd.startsWith("bj") || cmd.startsWith("bhist") || cmd.startsWith("BJ") || cmd.startsWith("count"))
	    return false;

	if( cmd.startsWith("\\") ) return string_is_to_be_kept( cmd.substring(1) );
	return true;
    }
}
