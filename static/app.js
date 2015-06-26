/**
 * Created by leona on 5/18/15.
 */
'use strict';
angular.module('gosaccoApp',['ngResource', 'ngRoute','formly','formlyBootstrap'])
.config(['$routeProvider','$locationProvider',function($routeProvider, $locationProvider){
      // $locationProvider.html5Mode(true);
      $routeProvider
      .when('/home',{
      	templateUrl:'views/home/home.html',
      	controller:'BaseCtrl'
      })
      .when('/members',{
      	templateUrl:'views/members/members.html',
      	controller:'MemberCtrl'
      })
      .when('/createMembers',{
      	templateUrl:'partials/members/createMember.html'
      })
      .when('/memberlogcategory',{
      	templateUrl:'partials/members/memberlogCategory.html'
      })
      .when('/membergroups',{
      	templateUrl:'partials/members/memberGroups.html'
      })
      .when('/nextofkinlist',{
      	templateUrl:'partials/members/nextofkinlist.html'
      })
      .when('/savings',{
      	templateUrl:'views/savings/savings.html',
      	controller:'DepositCtrl as vm'
      })
      .when('/deposit',{
            templateUrl:'partials/savings/deposit_savings.html',
            controller:'DepositCtrl as vm'
      })
      .when('/withdraw',{
            templateUrl:'partials/savings/withdraw_savings.html',
            controller:'WithdrawCtrl as vm'
      })
      .when('/list_savings',{
            templateUrl:'partials/savings/list_savings.html'
      })
      .when('/loans',{
      	templateUrl:'views/loans/loans.html',
      	// controller:'LoanCtrl'
      })
      .when('/loan_application',{
            templateUrl:'partials/loans/loan_application.html',
            controller:'LoanApplicationCtrl as vm'
      })
      .when('/loan_type',{
            templateUrl:'partials/loans/loan_type.html',
            controller:'LoanTypeCtrl as vm'
      })
      .when('/loan_form',{
            templateUrl:'partials/loans/loan_form.html',
            controller:'LoanFormCtrl as vm'
      })
      .when('/loan_list',{
            templateUrl:'partials/loans/loan_list.html'
      })
      .when('/loan_status',{
            templateUrl:'partials/loans/loan_status.html',

      })
      .when('/security',{
            templateUrl:'partials/loans/security.html',
            controller:'SecurityCtrl as vm'
      })
      .when('/security_article',{
            templateUrl:'partials/loans/security_article.html',
            controller:'SecurityArticleCtrl as vm'
      })
      .when('/shares',{
      	templateUrl:'views/shares/shares.html',
      	controller:'ShareCtrl'
      })
      .when('/others',{
      	templateUrl:'views/others/others.html',
      	controller:'OtherCtrl'
      })
      .when('/accounting',{
      	templateUrl:'views/accounting/accounting.html',
      	controller:'AccountingCtrl'
      })
      .when('/reports',{
      	templateUrl:'views/reports/reports.html',
      	controller:'ReportCtrl'
      })
      .when('/notifications',{
      	templateUrl:'views/notifications/notifications.html',
      	controller:'NotificationCtrl'
      })
      .when('/settings',{
      	templateUrl:'views/settings/settings.html',
      	controller:'SettingCtrl'
      }).otherwise({redirectTo:'/'});
    }]);