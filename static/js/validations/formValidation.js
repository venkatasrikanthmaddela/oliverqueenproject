/**
 * Created by narendra on 2/12/16.
 */

(function () {

    'use strict';

    angular.module('LoginFormApp',[]);

    angular.module('LoginFormApp')
        .controller('LoginController', LoginController)
        .controller('RegisterController', RegisterController);

    function LoginController($scope) {
        var login = this;
        $scope.login = "Avula";
    }

     function RegisterController($scope) {
        var register = this;
        $scope.regi = "Naidu";
    }

})();