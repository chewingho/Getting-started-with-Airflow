# Getting-started-with-Airflow

----	
## Description	
> 跟著youtube頻道 [Airflow - zero to hero](https://www.youtube.com/playlist?list=PLcoE64orFoVsyzbvfgiY5iNKo30fJ4IWm)，用Docker練習Airflow
## Process
1. 下載github上的[docker-compose-LocalExecutor.yml](https://github.com/puckel/docker-airflow/blob/master/docker-compose-LocalExecutor.yml)，另存成docker-compose.yml，並用指令啟動airflow  
```docker-compose up```
2. 建立DAG：my_sample_dag，練習python_operator、BranchPythonOperator、Xcom  
 *  Graph view：  
    run_this會透過xcom_push存入一個key為random_value、value為0-1任意數字的組合  
    branch_task有50%機率會呼叫say_hi_task，50%機率會呼叫say_hello_task  
    不論是say_hi_task或say_hello_task，皆會透過xcom_pull取得在run_this存入的value      
![my_sample_dag](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_sample_dag_graph_view.PNG)  
 *  xcom_push：key為random_value、value為0.924298520719721  
![xcom_push](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_sample_dag_XCom.PNG)  
 *  xcom_pull：取得value為0.924298520719721    
![xcom_pull](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_sample_dag_XCom2.PNG)  

3. 建立DAG：my_file_sample_dag，練習FileSensor、FSHook，偵測特定檔案是否存在，每隔1秒偵測1次，若嘗試10皆沒有偵測到，即失敗  
 *  Docker啟動後先手動建立Connection（因為用Docker啟動airflow，下次再啟動也必須重新建立）  
    將Conn id：my_tmp_file_path的path設定為/tmp  
![create_connection](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/create_connection.PNG) 
![show_connection](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/show_connection.PNG)  
 *  進入Docker容器內  
![interactive](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/interactive.PNG)  
 *  在/tmp建立test.txt  
![touch_file](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/touch_file.PNG)  
 *  先前沒有在/tmp放test.txt，因此sensing_task失敗，於上步驟建立檔案後再次執行Dag成功  
![success](https://github.com/chewingho/Getting-started-with-Airflow/blob/master/%E5%9C%96%E7%89%87/my_file_sample_dag_tree_view.PNG)  
## Reference
[apache/airflow](https://github.com/apache/airflow/blob/4f20f607764bb3477419321b5dfd0c53ba1db3c0/airflow/models.py#L1523)  
[hook](https://github.com/MTES-MCT/data-preparation-plugin)  


