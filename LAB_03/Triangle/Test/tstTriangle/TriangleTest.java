package tstTriangle;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import junit.framework.Assert;
import triangle.Triangle;

public class TriangleTest {
	
	
	private double parameterA, parameterB, parameterC;
	

	@Before
	public void setUp() throws Exception {
		
		
	}

	@After
	public void tearDown() throws Exception {
	}
	

	@Test
	public void checkTriangle_Correct_tst() {
		parameterA = 15;
		parameterB = 12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertTrue(triangle.checkTriangle());
		
	}
	
	@Test
	public void checkTriangle_Zero_A_tst(){
		parameterA = 0;
		parameterB = 12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}

	@Test
	public void checkTriangle_Zero_B_tst(){
		parameterA = 15;
		parameterB = 0;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	
	@Test
	public void checkTriangle_Zero_C_tst(){
		parameterA = 15;
		parameterB = 12;
		parameterC = 0;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	
	@Test
	public void checkTriangle_Negative_A_tst(){
		parameterA = -15;
		parameterB = 12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Negative_B_tst(){
		parameterA = 15;
		parameterB = -12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Negative_C_tst(){
		parameterA = 15;
		parameterB = 12;
		parameterC = -14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	
	@Test
	public void checkTriangle_Three_More_C_tst(){
		parameterA = 15;
		parameterB = 12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertTrue(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_More_B_tst(){
		parameterA = 15;
		parameterB = 12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertTrue(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_More_A_tst(){
		parameterA = 15;
		parameterB = 12;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertTrue(triangle.checkTriangle());
	}
	
	@Test
	public void checkTriangle_Three_Less_C_tst(){
		parameterA = 1;
		parameterB = 2;
		parameterC = 14;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_Less_B_tst(){
		parameterA = 5;
		parameterB = 12;
		parameterC = 1;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_Less_A_tst(){
		parameterA = 15;
		parameterB = 1;
		parameterC = 1;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_Equal_C_tst(){
		parameterA = 5;
		parameterB = 5;
		parameterC = 10;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_Equal_B_tst(){
		parameterA = 5;
		parameterB = 10;
		parameterC = 5;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	@Test
	public void checkTriangle_Three_Equal_A_tst(){
		parameterA = 10;
		parameterB = 5;
		parameterC = 5;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertFalse(triangle.checkTriangle());
	}
	
	@Test
	public void detectTriangle_Restangular_1_tst(){
		parameterA = 3;
		parameterB = 4;
		parameterC = 5;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 8);
	}
	@Test
	public void detectTriangle_Restangular_2_tst(){
		parameterA = 5;
		parameterB = 4;
		parameterC = 3;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 8);
	}
	@Test
	public void detectTriangle_Restangular_3_tst(){
		parameterA = 2;
		parameterB = 5;
		parameterC = 4;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 8);
	}
	
	@Test
	public void detectTriangle_Equilateral_tst(){
		parameterA = 2;
		parameterB = 2;
		parameterC = 2;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 0);
	}
	@Test
	public void detectTriangle_Isosceles_1_tst(){
		parameterA = 2;
		parameterB = 2;
		parameterC = 3;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 2);
		
	}
	@Test
	public void detectTriangle_Isosceles_2_tst(){
		parameterA = 3;
		parameterB = 2;
		parameterC = 2;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 2);
		
	}
	@Test
	public void detectTriangle_Isosceles_3_tst(){
		parameterA = 2;
		parameterB = 3;
		parameterC = 2;
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 2);
		
	}
	@Test
	public void detectTriangle_Isosceles_Restangular_tst(){
		parameterA = 2;
		parameterB = 2;
		parameterC = 2* Math.sqrt(2);
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 0);
		
	}
	@Test
	public void detectTriangle_Ordinary_tst(){
		parameterA = 1;
		parameterB = 3;
		parameterC = 8* Math.sqrt(2);
		Triangle triangle = new Triangle(parameterA, parameterB, parameterC);
		assertEquals(triangle.detectTriangle(), 4);
		
	}
	
	
	
}
