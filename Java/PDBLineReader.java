
public class PDBLineReader {

	private String line_;

	// Constructor
	public PDBLineReader( String S ) {
		line_ = S;
	}

	// Line Type
	public boolean isAtom() {
		if( line_.length() < 4 )
			return false;
		return line_.substring( 0, 4 ).equals( "ATOM" );
	}

	public boolean isTerminus() {
		return line_.substring( 0, 3 ).equals( "TER" );
	}

	public boolean isEndOfModel() {
		return line_.substring( 0, 6 ).equals( "ENDMDL" );
	}

	// Get Info
	public String getLine() {
		return line_;
	}

	public String getType() {
		return Extract( 0, 6 );
	}

	public int getAtomNumber() {
		if( isAtom() ) {
			try {
				return Integer.parseInt( Extract( 6, 11 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the atom number can not be parsed." );
				return -1;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the atom number is trying to be parsed." );
			return -1;
		}
	}

	public String getAtomName() {
		if( isAtom() ) {
			try {
				return Extract( 12, 16 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the atom name can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the atom name is trying to be parsed." );
			return null;
		}
	}

	public String getAlternateLocationIndicator() {
		if( isAtom() ) {
			try {
				return "" + line_.charAt( 16 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the alternate location indicator can not be parsed." );
				return null;
			}
		} else {
			System.err
					.println( line_ + " is not read as an ATOM but the alternate location indicator is trying to be parsed." );
			return null;
		}
	}

	public String getResidueName() {
		if( isAtom() ) {
			try {
				return Extract( 17, 20 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the residue name can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the residue name is trying to be parsed." );
			return null;
		}
	}

	public String getChainID() {
		if( isAtom() ) {
			try {
				return "" + line_.charAt( 21 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the chain identifier can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the chain identifier is trying to be parsed." );
			return null;
		}
	}

	public int getResidueNumber() {
		if( isAtom() ) {
			try {
				return Integer.parseInt( Extract( 22, 26 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the atom number can not be parsed." );
				return -1;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the atom number is trying to be parsed." );
			return -1;
		}
	}

	public String getAChar() {
		if( isAtom() ) {
			try {
				return "" + line_.charAt( 26 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the AChar can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the AChar is trying to be parsed." );
			return null;
		}
	}

	public double getPositionX() {
		if( isAtom() ) {
			try {
				return Double.parseDouble( Extract( 30, 38 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the x coordinate can not be parsed." );
				return Double.NEGATIVE_INFINITY;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the x coordinate is trying to be parsed." );
			return Double.NEGATIVE_INFINITY;
		}
	}

	public double getPositionY() {
		if( isAtom() ) {
			try {
				return Double.parseDouble( Extract( 38, 46 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the y coordinate can not be parsed." );
				return Double.NEGATIVE_INFINITY;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the y coordinate is trying to be parsed." );
			return Double.NEGATIVE_INFINITY;
		}
	}

	public double getPositionZ() {
		if( isAtom() ) {
			try {
				return Double.parseDouble( Extract( 46, 54 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the z coordinate can not be parsed." );
				return Double.NEGATIVE_INFINITY;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the z coordinate is trying to be parsed." );
			return Double.NEGATIVE_INFINITY;
		}
	}

	public double getOccupancy() {
		if( isAtom() ) {
			try {
				return Double.parseDouble( Extract( 54, 60 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the occupancy can not be parsed." );
				return Double.NEGATIVE_INFINITY;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the occupancy is trying to be parsed." );
			return Double.NEGATIVE_INFINITY;
		}
	}

	public double getTemperatureFactor() {
		if( isAtom() ) {
			try {
				return Double.parseDouble( Extract( 60, 66 ) );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the temperature factor can not be parsed." );
				return Double.NEGATIVE_INFINITY;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the temperature factor is trying to be parsed." );
			return Double.NEGATIVE_INFINITY;
		}
	}

	public String getSegmentID() {
		if( isAtom() ) {
			try {
				return Extract( 72, 76 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the segment identifier can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the segment identifier is trying to be parsed." );
			return null;
		}
	}

	public String getElement() {
		if( isAtom() ) {
			try {
				return Extract( 76, 78 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the chemical element can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the chemical element is trying to be parsed." );
			return null;
		}
	}

	public String getCharge() {
		if( isAtom() ) {
			try {
				return Extract( 78, 80 );
			}
			catch( Exception E ) {
				System.err.println( line_ + " is read as an ATOM but the charge can not be parsed." );
				return null;
			}
		} else {
			System.err.println( line_ + " is not read as an ATOM but the charge is trying to be parsed." );
			return null;
		}
	}

	// Set Info
	public void setLine( String NEW ) {
		line_ = NEW;
	}

	public void setType( String NEW ) {
		Rewrite( Repack( NEW, true, 6 ), 0 );
	}

	public void setAtomNumber( int i ) {
		if( i > 99999 ) {
			System.err.println( "Can not create more than 99999 atoms" );
			return;
		}

		Rewrite( Repack( i + "", false, 5 ), 6 );
		// TODO
	}

	public void setAtomName( String NEW ) {
		System.err.println( "PDBLineReader.set_ATOM_NAME has not yet been written. Sorry" );
	}

	public void setResidueName( String NEW ) {
		Rewrite( NEW, 17 );// TODO I wrote this really quickly, needs more work
	}

	public void setAlternateLocationIndicator() {
		// TODO
	}

	public void setChainID() {
		// TODO
	}

	public void setResidueNumber( int i ) {
		if( i > 9999 ) {
			System.err.println( "Can not create more than 9999 residues" );
			return;
		}

		Rewrite( Repack( i + "", false, 4 ), 22 );
	}

	public void setAChar() {
		// TODO
	}

	public void setPositionX() {
		// TODO
	}

	public void setPositionY() {
		// TODO
	}

	public void setPositionZ() {
		// TODO
	}

	public void setOccupancy() {
		// TODO
	}

	public void setTemperatureFactor() {
		// TODO
	}

	public void setSegmentID() {
		// TODO
	}

	public void setElement() {
		// TODO
	}

	public void setCharge() {
		// TODO
	}

	// Utilities
	public final String Extract( int start, int end ) {
		return remove_chars( line_.substring( start, end ), new char[] { ' ' } );
	}

	public final void Rewrite( String NEW, int location_of_first_char ) {
		line_ = line_.substring( 0, location_of_first_char ) + NEW
				+ line_.substring( location_of_first_char + NEW.length() );
	}

	public final static String Repack( Object O, boolean add_to_right_side, int length ) {

		String NEW = O.toString();
		if( NEW.length() > length ) {
			System.err.println( NEW + " is longer than " + length );
			return null;
		}

		while ( NEW.length() < length ) {
			if( add_to_right_side ) {
				NEW = NEW + " ";
			} else {
				NEW = " " + NEW;
			}
		}

		return NEW;

	}

	public final static String remove_chars( String IN, char[] bad ) {

		String OUT = "";

		outerloop:
		for( int i = 0; i < IN.length(); i++ ) {
			for( char C : bad ){
				if( IN.charAt( i ) == C ){
					continue outerloop;
				}
			}
			OUT += IN.charAt( i );
		}

		return OUT;
	}

	// TESTING:
	public static void main( String[] args ) {
		PDBLineReader Paul = new PDBLineReader(
				"ATOM      1  N   TRP A   1       2.304 -17.099  24.233  1.00  0.00           N" );
		System.out.println( Paul.getLine() );
		Paul.setAtomNumber( 502 );
		Paul.setResidueNumber( 50 );
		System.out.println( Paul.getLine() );
	}
}
