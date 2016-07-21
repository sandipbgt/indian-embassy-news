(function() {
    'use strict';

    angular
        .module('embassyApp', [
            'app.routes',
            'article'
            ])
        .constant('CONFIG', {
          "BASE": "http://localhost:5000",
          "BASE_API": "http://localhost:5000/api"
        });
})();