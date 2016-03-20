'use strict';

/**
 * @ngdoc function
 * @name companyDkApp.controller:EditCtrl
 * @description
 * # EditCtrl
 * Controller of the companyDkApp
 */
angular.module('companyDkApp')
  .controller('EditCtrl', ['$scope', '$http', 'Flash', '$routeParams', function($scope, $http, Flash, $routeParams) {
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

        var saveCompany = function(data) {
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

        var deleteCompany = function(data) {
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
                    params: {
                        page:  $scope.page,
                        count: $scope.count
                    }
                })
            .then(function(response){
                $scope.company = response.data.data;
            });
        }

        $scope.successAlert = function () {
            var message = '<strong>Well done!</strong> The Company was modified';
            var id = Flash.create('success', message, 0, {class: 'alert', id: 'alert'}, true);
        };

        $scope.deleteAlert = function () {
            var message = '<strong>Bye bye!</strong> The Company was deleted';
            var id = Flash.create('danger', message, 0, {class: 'alert', id: 'alert'}, true);
        };

        $scope.save = function() {
            var data = buildData();
            saveCompany(data);
        };

        $scope.delete = function() {
            deleteCompany($routeParams.id);
        };

        loadCompany();
  }]);
