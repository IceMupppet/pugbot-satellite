angular.module('nodePugbot', [])
.controller('mainController', ($scope, $http) => {
  $scope.formData = {};
  $scope.coordData = {};
  $scope.pugbotData = {};
  // Get all todos
  $http.get('/api/v1/pugbot')
  .success((data) => {
    $scope.pugbotData = data;
    console.log(data);
  })
  .error((error) => {
    console.log('Error: ' + error);
  });
  // Get all coords
  $http.get('/api/v1/coords')
  .success((data) => {
    $scope.coordData = data;
    console.log(data);
  })
  .error((error) => {
    console.log('Error: ' + error);
  });
  // Create a new todo
  $scope.createPugbot = () => {
    $http.post('/api/v1/pugbot', $scope.formData)
    .success((data) => {
      $scope.formData = {};
      $scope.pugbotData = data;
      console.log(data);
    })
    .error((error) => {
      console.log('Error: ' + error);
    });
  };
  // Delete a todo
  $scope.deletePugbot = (pugbotID) => {
    $http.delete('/api/v1/pugbot/' + pugbotID)
    .success((data) => {
      $scope.pugbotData = data;
      console.log(data);
    })
    .error((data) => {
      console.log('Error: ' + data);
    });
  };
});
