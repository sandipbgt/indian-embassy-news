(function() {
    'use strict';

    angular
        .module('article.controllers')
        .controller('articleHomeController', articleHomeController);

        articleHomeController.$inject = ['Article'];

        function articleHomeController(Article) {
            var self = this;
            // self.articles = articles.data;
            //console.log(articles);
            self.loading = true;
            Article.all()
                .success(function(data) {
                    console.log(data);
                    self.articles = data;
                    self.loading = false;
                })
                .error(function(data) {
                    console.log(data);
                })
        }
})();