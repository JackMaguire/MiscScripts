import javax.imageio.*;
import java.awt.*;
import java.awt.image.*;
import java.io.*;
import com.github.sarxos.webcam.Webcam;

public class TakeSnapShot {

    public static void main(String[] args) throws IOException{
		
	Webcam w = Webcam.getDefault();
	w.getDevice().setResolution( new Dimension( 1280, 720 ) );
	w.open();

	String desitination_filename = "Snapshot.png";
	ImageIO.write( w.getImage(), "png", new File( destination_filename ) );
	w.close();
    }
	
}
