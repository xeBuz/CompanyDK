'use strict';

/**
 * @ngdoc overview
 * @name CompanyDK
 * @description
 * # CompanyDKApp
 *
 * Main module of the application.
 */
angular
  .module('CompanyDK', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'LocalStorageModule',
    'API'
  ])
  .config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  	$routeProvider
  	  .when('/', {
  	  	templateUrl: 'static/partials/index.html',
  	  	controller: IndexController
  	  })
  	  .when('/about', {
  	  	templateUrl: 'static/partials/about.html',
  	  	controller: AboutController
  	  })
  	  .when('/companies/', {
  	  	templateUrl: 'static/partials/companies.html',
  	  	controller: CompaniesController
  	  })
  	  .when('/company/:id', {
  	  	templateUrl: '/static/partials/company-detail.html',
  	  	controller: CompanyDetailController
  	  })
  	  .otherwise({
  	  	redirectTo: '/'
  	  })
  	;
  	$locationProvider.html5Mode(true);
  }])
;



  //.config(function ($httpProvider) {
  //  $httpProvider.defaults.useXDomain = false;
  //  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  //  $httpProvider.defaults.headers.put['Content-Type'] = 'application/x-www-form-urlencoded';
  //
  //  delete $httpProvider.defaults.headers.common['X-Requested-With'];
  //})