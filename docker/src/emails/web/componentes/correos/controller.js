
app.controller("PerfilCtrl", ["$scope", "$resource", "$location", function ($scope, $resource, $location) {

  var Correo = $resource('http://127.0.0.1:7001/emails/api/v1.0/correos/:id', {id:null});

  var correos = Correo.query(function(cs,resp) {
    $scope.correos = cs;
  })

}]);
