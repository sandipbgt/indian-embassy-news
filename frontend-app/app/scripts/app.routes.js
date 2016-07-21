(function() {
    angular
        .module('app.routes', ['ui.router'])
        .config(['$stateProvider', '$urlRouterProvider',
            function($stateProvider, $urlRouterProvider) {
                $stateProvider
                    .state('home', {
                        url: '/',
                        templateUrl: 'views/article/home.html',
                        controller: 'articleHomeController',
                        controllerAs: 'articleHomeCtrl'
                    });
                
                $urlRouterProvider.otherwise('/');
            }
        ]);
})();