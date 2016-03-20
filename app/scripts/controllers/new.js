'use strict';

/**
 * @ngdoc function
 * @name companyDkApp.controller:NewCtrl
 * @description
 * # NewCtrl
 * Controller of the companyDkApp
 */
angular.module('companyDkApp')
  .controller('NewCtrl', ['$scope', '$http', 'Flash', function($scope, $http, Flash) {
        $scope.country = {};
        $scope.pageTitle = "New Company";
        $scope.buttonText = "Add";
        $scope.showDelete = false;

        $scope.url = 'http://0.0.0.0:5000/api/companies';

        var buildData = function(){
            return {
                'name': $scope.company.name || null,
                'address': $scope.company.address || "N/A",
                'city': $scope.company.city || "N/A",
                'country': $scope.company.country || "N/A",
                'phone': $scope.company.phone || null,
                'email': $scope.company.email || null
            };
        };

        var saveCompany = function(data) {
            $http(
                {
                    method: 'POST',
                    url: $scope.url,
                    data: $.param(data),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                })
            .then(function(response) {
                if (response.status === 201){
                    $scope.successAlert();
                }
            });
        };

        $scope.successAlert = function () {
            var message = '<strong>Well done!</strong> The new Company was created';
            var id = Flash.create('success', message, 0, {class: 'alert', id: 'alert'}, true);
        };

        $scope.save = function() {
            var data = buildData();
            saveCompany(data);
        };
  }]);
