app = angular.module('MainApp', ['ngRoute', 'ngResource'])

app.config(['$routeProvider', function($routeProvider) {

  $routeProvider
    .when('/correos/:id', {templateUrl: '/componentes/correos/index.html', controller:'CorreosCtrl'})
    .when('/correos', {templateUrl: '/componentes/correos/index.html', controller:'CorreosCtrl'})
    .otherwise({ redirectTo: '/correos' });

}]);

app.config(['$resourceProvider', function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
