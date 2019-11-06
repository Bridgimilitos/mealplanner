package main;

import com.dieselpoint.norm.Database;

import entity.Ingredient;

public final class Main 
{

	public static void main(String[] args) 
	{
	    Database db = new Database();
	    db.setDatabaseName("MealPlanner");
	    db.setDataSourceClassName("com.microsoft.sqlserver.jdbc.SQLServerDataSource");
	    db.setServerName("localhost");
	    db.setUser("sa");
	    db.setPassword("q6lp1LUkUkPQW24vxPgUVdBv");
	    
	    Ingredient ham = new Ingredient("ham", "g");
	    db.insert(ham);
	}

}
