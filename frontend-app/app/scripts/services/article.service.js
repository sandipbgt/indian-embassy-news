(function() {
	'use strict';

	angular
		.module('article.services')
		.factory('Article', Article);

		/**
		* Article factory
		*/

		Article.$inject = ['CONFIG', '$http'];

		function Article(CONFIG, $http) {
			var Article = {
				all: all
			};

			return Article;

		function all() {
			return $http.get(CONFIG.BASE_API + '/articles');
		}
	}
})();