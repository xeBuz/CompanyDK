'use strict';

/**
 * @ngdoc function
 * @name companyDkApp.controller:EditCtrl
 * @description
 * # EditCtrl
 * Controller of the companyDkApp
 */
angular.module('companyDkApp')
  .controller('EditCtrl', ['$scope', '$http', 'Flash', '$routeParams', '$location', function($scope, $http, Flash, $routeParams, $location) {
        $scope.country = {};
        $scope.pageTitle = "Company ID: " + $routeParams.id;
        $scope.buttonText = "Edit";
        $scope.showDelete = true;

        $scope.url = 'http://0.0.0.0:5000/api/companies/' + $routeParams.id;

        var buildData = function(){
            return {
                'name': $scope.company.name || null,
                'address': $scope.company.address || null,
                'city': $scope.company.city || null,
                'country': $scope.company.country || null,
                'phone': $scope.company.phone || null,
                'email': $scope.company.email || null
            };
        };

        var editCompany = function(data) {
            $http(
                {
                    method: 'PUT',
                    url: $scope.url,
                    data: $.param(data),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                })
            .then(function(response) {
                if (response.status === 200){
                    $scope.successAlert();
                }
            });
        };

        var deleteCompany = function() {
            $http(
                {
                    method: 'DELETE',
                    url: $scope.url
                })
            .then(function(response) {
                if (response.status === 200){
                    $scope.deleteAlert();
                }
            });
        };

        var loadCompany = function() {
            $http(
                {
                    method: 'GET',
                    url: $scope.url,
                })
            .then(function(response){
                $scope.company = response.data.data;
            }, function errorCallback(response) {

                if (response.status === 404) {
                    $location.path('404');
                }
            });
        };

        $scope.successAlert = function () {
            var message = '<strong>Well done!</strong> The Company was modified';
            Flash.create('success', message, 0, {class: 'alert', id: 'alert'}, true);
        };

        $scope.deleteAlert = function () {
            var message = '<strong>Bye bye!</strong> The Company was deleted';
            Flash.create('danger', message, 0, {class: 'alert', id: 'alert'}, true);
        };

        $scope.save = function() {
            var data = buildData();
            editCompany(data);
        };

        $scope.delete = function() {
            deleteCompany();
        };

        loadCompany();
  }]);
