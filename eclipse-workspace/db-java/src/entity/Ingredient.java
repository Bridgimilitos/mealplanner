package entity;

import java.util.UUID;

import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@Table(name="Ingredient")
public final class Ingredient 
{
	@Id
	@GeneratedValue
	private UUID id = null;
	
	@Column(name="Ingredient")
	private String ingredient = "";
	
	@Column(name="Unit")
	private String unit = "";

	public Ingredient()
	{
		//Empty
	    //Tastey testy ingredients
	}
	
	public Ingredient(String ingredient, String unit)
	{
		this.ingredeint = ingredient;
		this.unit = unit;
	}
}
