var APC = angular.module('APC', []);

APC.controller('maincontroller', ['$scope','$http', function($scope, $http) {
    $scope.process={};
    $scope.newprocess={};
    $scope.processtag={};
    $scope.tag={};
    $scope.tagmap={};

    $scope.proparamType=['Input','Output'];
    $scope.proparams={};
	$scope.newproparam={};
	$scope.proparamsource={};
	$scope.proparammap={};
	$scope.proparamprocess={};


	$scope.model={};
	$scope.newmodel={};
	$scope.modelprocess={};

	$scope.file={};
	$scope.newfile={};
	$scope.filemap={};


	$scope.sourcetype=['Manual','Digital','Historical'];
	$scope.newsourcetype={};
   /* $scope.init =function(){                    //initialization function
      $http.get('http://127.0.0.1:8000/api/Process/').then(function (response){
          if(response.status==200)
          {
            $scope.process=response.data;
            prolen=Object.keys($scope.process).length;
          }
    });
    $http.get('http://127.0.0.1:8000/api/FileUpload/').then(function (response){
          if(response.status==200)
          {
            $scope.file=response.data;
          }
    });

    $http.get('http://127.0.0.1:8000/api/ProcessParameters/').then(function (response){
          if(response.status==200)
          {
            $scope.proparams=response.data;
          }
    });

    $http.get('http://127.0.0.1:8000/api/Tag/').then(function (response){
          if(response.status==200)
          {
            $scope.tag=response.data;
          }
    });
    $http.get('http://127.0.0.1:8000/api/PredictionModel/').then(function (response){
          if(response.status==200)
          {
            $scope.model=response.data;
          }
    });
    $http.get('http://127.0.0.1:8000/api/FileUpload/').then(function (response){
          if(response.status==200)
          {
            $scope.file=response.data;
          }
    });
  }
	$scope.upload = function(e){
    $scope.newfile.file = e.files[0];          //to assign file to fileupload model on change
	}


    $scope.redirect1 = function(){
    alert("Posted");
    window.location("BusinessUser.html");       //to redirect after hitting submit
    }
    $scope.redirect2 = function(){
    alert("Posted");
    window.location("Developer.html");       //to redirect after hitting submit
    }


	$scope.submitForm = function() {                            //to update new process metadata in database and populate tagmap table
	$scope.tagmap.TagID=$scope.processtag.id;
	var count = Object.keys($scope.process).length;
	$scope.tagmap.ProcessID=$scope.process[count-1].id+1;           //to create tagmap object for insertion in database
    $http.post('http://127.0.0.1:8000/api/Process/', $scope.newprocess);
    $http.get('http://127.0.0.1:8000/api/Process/');
    $http.post('http://localhost:8000/api/TagMap/', $scope.tagmap).then(function (response){
          if(response.status==200)
          {
            $scope.redirect1();
          }
    });
    }*/
    
    $scope.test = function() { console.log("dk.fjn");
    var fileReader = new FileReader();
    filetext=fileReader.readAsText('D:\training\ML\andr-ng\machine-learning-ex3\ex3\New Text Document.txt');
    //console.log(filetext);
    
    
    }

    /*$scope.submitForm2 = function() {

    var count = Object.keys($scope.proparams).length;
	$scope.newproparam.source = $scope.proparamsource.id;
	$scope.proparammap.ProcessID=$scope.proparamprocess.id;
	$scope.proparammap.ProcessParametersID=$scope.proparams[count-1].id+1;

    console.log($scope.proparammap);

    $http.post('http://127.0.0.1:8000/api/ProcessParameters/',$scope.newproparam);
    $http.get('http://127.0.0.1:8000/api/ProcessParameters/',$scope.newproparam);
    $http.post('http://127.0.0.1:8000/api/ProcessParametersMap/',$scope.proparammap).then(function (response){
          if(response.status==200)
          {
            $scope.redirect1();
          }
    });;

     }

    $scope.submitForm3 = function() {


   // $scope.newfile.name=$scope.newfile.file.name;
    var formdata= new FormData;
    var file=$('#modelfile')[0].files[0];
    formdata.append('file',file);
    formdata.append('name',$scope.newfile.file.name);
    console.log(formdata);
    $http.post('http://127.0.0.1:8000/api/FileUpload/',formdata, {transformRequest:angular.identity,headers:{'Content-Type':undefined}}).then(function(res){
        
    });

    $scope.newmodel.ProcessID=$scope.modelprocess.id;
    $http.post('http://127.0.0.1:8000/api/PredictionModel/',$scope.newmodel);

    var count = Object.keys($scope.model).length;
    $scope.filemap.PredictionModelID=$scope.model[count-1].id+1;
    count = Object.keys($scope.file).length;
    $scope.filemap.FileUploadID=$scope.file[count-1].id+1;
    
    console.log($scope.filemap);

    $http.get('http://127.0.0.1:8000/api/PredictionModel/');
    $http.get('http://127.0.0.1:8000/api/FileUpload/');
    $http.post('http://127.0.0.1:8000/api/FileMap/',$scope.filemap).then(function (response){
          if(response.status==200)
          {
            $scope.redirect2();
          }
    });


        }

        $scope.execute = function(){};

*/}]);


  
