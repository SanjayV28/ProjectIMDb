# Transforming data in the data warehouse

We have our raw data loaded into our data warehouse so far. We will now transform these raw data and make it available for analytics and building dashboards. In this project, I have used Data Build Tool(DBT) for transformation the data. If you like to proceed with the same, Kindly follow the below steps!

## DBT Setup
- The first step is to create a DBT account [here](https://www.getdbt.com/signup/).
- Create a service account for DBT to access the bigquery and grant viewer and BigQuery admin access to the service account. Now that the service account has been created we need to add and download a JSON key, go to the keys section, select "create new key". Select key type JSON and once you click on create it will get inmediately downloaded for you to use.
  >**Note:** Instead of using a new service account for DBT, You can also use the service account we created earlier for other services by adding viewer access to it.
- Setup the new project
  1. Create a project and name you project
  2. Set up a Database Connection - **Choose BigQuery**. On the setting page, Upload the json key you downloaded for DBT service account. This will fill out most fields related to the production credentials. Scroll down to the end of the page and enter your dataset name.
     >**Note:** The dataset you'll enter under the development credentials is the one you'll use to run and build your models during development.
  3. Click on test to test your connection to the Bigquery.
- Now the connection is established, You can add your github repository by choosing managed repository and provide a name.
- Finally, we can review our project settings and make sure that everything is set.
- You can also check out the same instructions mentioned [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/00caff1b661bcadecb82f960ee92c917362fa3c0/week_4_analytics_engineering/dbt_cloud_setup.md).

## Development
- Once we have completed the setup. Click on the **Start Developing** tab on the left side which will take you to the project IDE.
- 
