# Getting-started-with-Airflow

----	
## Description	
> 跟著youtube頻道 [Airflow - zero to hero](https://www.youtube.com/playlist?list=PLcoE64orFoVsyzbvfgiY5iNKo30fJ4IWm)，用Docker練習Airflow
## Process
1. pull [docker-compose.yml](https://github.com/puckel/docker-airflow/blob/master/docker-compose-LocalExecutor.yml)  
2. 建立DAG:my_sample_dag，練習python_operator、BranchPythonOperator、Xcom  
 -2.1 Graph view   
![my_sample_dag](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_sample_dag_graph_view.PNG)  
 -2.2 xcom_push  
![xcom_push](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_sample_dag_XCom.PNG)  
 -2.3 xom_pull  
![xcom_pull](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_sample_dag_XCom2.PNG)  

3. 建立DAG:my_file_sample_dag，練習FileSensor、FSHook
 -3.1 Docker啟動後先手動建立Connection  
![create_connection](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/create_connection.PNG)  
![show_connection](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/show_connection.PNG)  
 -3.2 進入Docker容器內  
![interactive](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/interactive.PNG)  
 -3.3 在/tmp建立test.txt  
![touch_file](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/touch_file.PNG)  
 -3.4 成功執行DAG  
![success](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_file_sample_dag_tree_view.PNG)  


