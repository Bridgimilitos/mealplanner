USE MealPlanner

USE [master]
GO
ALTER DATABASE [MealPlanner] SET READ_COMMITTED_SNAPSHOT ON WITH NO_WAIT
GO
ALTER DATABASE [MealPlanner] SET ALLOW_SNAPSHOT_ISOLATION ON
GO

/****** Script for SelectTopNRows command from SSMS  ******/
INSERT INTO Recipe (RecipeName, RecipeSource, Serves, VegetarianStatus, Mushrooms, Calories, CookTime)
SELECT [Name]
      ,ISNULL([Source], '')
      ,CASE WHEN [Serves] > 255 THEN 4 ELSE ISNULL([Serves], 0) END
      ,ISNULL([Vegetarian Status],'')
      ,CASE WHEN [Mushrooms] = 'Yes' THEN 1 ELSE 0 END
      ,ISNULL([Calories per serving], -1)
      ,ISNULL([Time to cook], -1)
  FROM [MealPlanner].[dbo].[Recipes]

  SELECT * FROM Recipe

INSERT INTO Ingredient (Ingredient, Unit )
SELECT Name AS Ingredient, Unit 
FROM Imported_Ingredients

INSERT INTO VegetarianStatus (Status) VALUES ('Vegetarian'), ('Vegan'), ('Pescetarian'), ('Meat')

SELECT * FROM VegetarianStatus

BEGIN TRANSACTION
UPDATE Recipe 
SET IdVegStatus = v.Id
FROM Recipe r,
	 VegStatus v
WHERE r.VegetarianStatus = v.Status
--COMMIT

SELECT * FROM Imported_IngredientForRecipe

INSERT INTO RecipeIngredientLink (IdRecipe, IdIngredient, Quantity)
SELECT r.Id AS IdRecipe, 
	   i.Id AS IdIngredient,
	   ISNULL(ir.Quantity, 1)
FROM Imported_IngredientForRecipe ir,
	 Recipe r,
	 Ingredient i
WHERE r.RecipeName = ir.Recipe
AND i.Ingredient = ir.Ingredient
