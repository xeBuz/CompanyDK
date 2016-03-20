'use strict';

/**
 * @ngdoc function
 * @name companyDkApp.controller:ListCtrl
 * @description
 * # ListCtrl
 * Controller of the companyDkApp
 */
angular.module('companyDkApp')
  .controller('ListCtrl', ['$scope', '$http', function($scope, $http) {

        $scope.companyList = [];
        $scope.url = 'http://0.0.0.0:5000/api/companies';
        $scope.page = 1;
        $scope.count = 5;

        $scope.hasNext = null;
        $scope.hasPrev = null;

        var getCompanies = function() {
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
                $scope.companyList = response.data.data;

                $scope.hasNext = !angular.isUndefined(response.data.links.next);
                $scope.hasPrev = !angular.isUndefined(response.data.links.prev);

            });
        };

        $scope.openCompany = function(company) {
            console.log(company);
            console.log(company.id);
        };

        $scope.nextPage = function() {
            $scope.page++;
            getCompanies();
        };

        $scope.prevPage = function() {
            $scope.page--;
            getCompanies();
        };

        getCompanies();
}]);