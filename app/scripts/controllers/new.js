'use strict';

/**
 * @ngdoc function
 * @name companyDkApp.controller:NewCtrl
 * @description
 * # NewCtrl
 * Controller of the companyDkApp
 */
angular.module('companyDkApp')
  .controller('NewCtrl', ['$scope', '$http', function($scope, $http) {
        $scope.country = {};
        $scope.pageTitle = "New Company";
        $scope.buttonText = "Add";

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
            console.log(data);
            $http(
                {
                    method: 'POST',
                    url: $scope.url,
                    data: $.param(data),
                    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                })
            .then(function(response) {
                if (response.status == 201){
                    console.log("SUCCESS");
                }
            });
        };

        $scope.save = function() {
            var data = buildData();
            saveCompany(data);
        };
  }]);
