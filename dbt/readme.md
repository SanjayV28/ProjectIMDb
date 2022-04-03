# Transforming data in the data warehouse

We have our raw data loaded into our data warehouse so far. We will now transform these raw data and make it available for analytics and also for building dashboards. In this project, I have used **Data Build Tool(DBT)** for transforming the data. If you like to proceed with the same, Kindly follow the below steps!

## DBT Setup
- The first step is to create a DBT account [here](https://www.getdbt.com/signup/).
- Create a service account for DBT to access the bigquery and grant viewer and BigQuery admin access to the service account. Now that the service account has been created we need to add and download a JSON key, go to the keys section, select "create new key". Select key type JSON and once you click on create it will get inmediately downloaded for you to use.
  >**Note:** Instead of using a new service account for DBT, You can also use the service account we created earlier for other services by adding viewer access to it.
- Setup the new project
  - Create a project and name your project
  - Set up a Database Connection - **Choose BigQuery**. On the setting page, Upload the json key you downloaded for the DBT service account. This will fill out most fields related to the development credentials. Scroll down to the end of the page and enter your dataset name.
     >**Note:** The dataset you'll enter under the development credentials is the one you'll use to run and build your models during development.
  - Click on test to test your connection to the Bigquery.
- Now the connection is established, You can add your github repository by choosing managed repository and provide a name.
- Finally, we can review our project settings and make sure that everything is set.
- You can also check out the same instructions mentioned [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/00caff1b661bcadecb82f960ee92c917362fa3c0/week_4_analytics_engineering/dbt_cloud_setup.md).

## Development
- Once we have completed the setup. Click on the `Start Developing` tab on the left side which will take you to the project IDE. Now we will start transforming our data.
- Click on `initialize project` tab on the top left side which will populate the basic directory with the required files and folders.
- Under the models folder, delete the subfolder `example` and create two new subfolders `staging` and `core`.
- Click on the `dbt_project.yml` and update the project name and add materialized settings to the two newly created models subfolders. By doing so, we are informing the DBT to create all models as views under staging and create all models as tables under core. 
- Under the `staging` folder, create five new files called **schema.yml, stgtitleakas.sql, stgtitlebasics.sql, stgtitleepisode.sql and stgtitleratings.sql**.
- In the `schema.yml` file, We are defining the essential tests and documentation for our models stgtitleakas.sql, stgtitlebasics.sql, stgtitleepisode.sql and stgtitleratings.sql.
- In the `stgtitleakas.sql`, `stgtitlebasics.sql`, `stgtitleepisode.sql`, and `stgtitleratings.sql` files, We are replacing the alpha numeric values in few columns and typecasting all columns to the right data type.
- Under the `core` folder, create two new files called **schema.yml and facttitletable.sql**
- In the `schema.yml` file, We are defining the essential tests and documentation for our model facttitletable.sql.
- In the `facttitletable.sql` file, We are selecting the required columns by joining the stgtitleakas.sql, stgtitlebasics.sql, stgtitleepisode.sql, and stgtitleratings.sql based on the titleID column to make a desired table.
  ![DBT flow](https://github.com/SanjayV28/ProjectIMDb/blob/4eebe46e5e7a57eb872c39a85dda7157d4304ba5/images/DBT.png)
- Now, we can run and test our models using the command `dbt build` at the bottom which will complete the mentioned tests in the `schema.yml` files and build the models under the `staging` BigQuery dataset if there are no errors returned.
- Finally, we can click the `commit` icon on the top left to commit our changes in the repository.

## Production Deployment
- Now We have successfully completed the transformations in `development` environment, We can replicate the same in the `production` environment which will be available for our analysts and BI developers for their use.
- The first step is to create a production environment. To do this, Click on the top left side menu and select the Environments tab. Then click on the New Environments and enter the following:
  - Name: Your environment name(e.g. Production).
  - Type: Deployment.
  - Credentials Schema: Your prod dataset name(e.g. production).
- Now we have our production environment ready, We can create a new job and name your job and set this production to it. In the job configurartion settings, enter the following:
  - Select the Genrate docs to document our work. 
  - Enter the `dbt test` and `dbt run` commands under the commands tab to test and run our models.
  - Schedule this job to run every 12 hours. So the job will run twice a day.
- Finally save the job and maually run to make sure our models are created under production BigQuery dataset.

**_Congratulations, Now we have successfully transformed our data based on the requirements and made it available for further analytics and visualisations!!_**
