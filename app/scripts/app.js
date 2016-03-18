'use strict';

/**
 * @ngdoc overview
 * @name companyDkApp
 * @description
 * # companyDkApp
 *
 * Main module of the application.
 */
angular
  .module('companyDkApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'angular-loading-bar'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/list', {
        templateUrl: 'views/list.html',
        controller: 'ListCtrl',
        controllerAs: 'list'
      })
      .when('/new', {
        templateUrl: 'views/new.html',
        controller: 'NewCtrl',
        controllerAs: 'new'
      })

      .otherwise({
        redirectTo: '/'
      });
  });
