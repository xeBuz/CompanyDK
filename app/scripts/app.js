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
    'angular-loading-bar',
    'ngFlash'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/list', {
        templateUrl: 'views/list.html',
        controller: 'ListCtrl',
        controllerAs: 'list'
      })
      .when('/new', {
        templateUrl: 'views/country.html',
        controller: 'NewCtrl',
        controllerAs: 'new'
      })
      .when('/edit/:id', {
        templateUrl: 'views/country.html',
        controller: 'EditCtrl',
        controllerAs: 'edit'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .config(function ($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $httpProvider.defaults.headers.put['Content-Type'] = 'application/x-www-form-urlencoded';

    delete $httpProvider.defaults.headers.common['X-Requested-With'];
  });
