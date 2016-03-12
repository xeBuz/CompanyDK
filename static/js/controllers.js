'use strict';

/* Controllers */

function IndexController($scope) {
	console.log("INDEX");
}

function AboutController($scope) {
	console.log("ABOUT");
}

function CompaniesController($scope, API) {
	//var postsQuery = Post.get({}, function(posts) {
	//	$scope.posts = posts.objects;
	//});
	console.log("COMPANIES");

}

function CompanyDetailController($scope, $routeParams, API) {
	//var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
	//	$scope.post = post;
	//});
	console.log("DETAIL");
}
