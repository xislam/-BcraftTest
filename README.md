# BcraftTest

#Монолог 
    Это тестовое задание интерестно тем что тем что атвет там же ывсе написано 
    от меня тока это написать в коде хммм прикольно  
    

#Запуск 
    
  надо запустить докер 
    
    docker-compose
    
    
#URL 
    
    admin/
    api-auth/
    
 Для получения списка    
    
    api_v1/statistics/
    
 Детальный просмотр  
     
    api_v1/statistics/<int:pk>
    
 Фильт периуда 
    
    api_v1/filter/

пример 
    
    http://127.0.0.1:8000/api_v1/filter/?start_date=2021-12-15&end_date=2021-12-15
