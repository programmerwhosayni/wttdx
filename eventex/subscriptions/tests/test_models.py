# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Arthur Silva',
            cpf='12345678901',
            email='arthur@silva.com.br',
            phone='21-87654321'
         )

    def test_create(self):
        'Subscription mus have name, cpf, email, phone.'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Arthur Silva', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Arthur Silva', cpf='12345678901',
                                    email='arthur@silva.com.br', phone='21-87654321')

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Arthur Silva', cpf='12345678901',
                         email='outro@email.com', phone='21-87654321')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Arthur Silva', cpf='00000000011',
                         email='arthur@silva.com.br', phone='21-87654321')
        self.assertRaises(IntegrityError, s.save)
