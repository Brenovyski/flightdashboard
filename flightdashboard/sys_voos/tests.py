from django.test import TestCase

from sys_voos.models import CompanhiaAerea, Voo, Partida, Chegada

class CompanhiaAereaTest(TestCase):
  @classmethod
  def setUpTestData(cls):
      CompanhiaAerea.objects.create(nome='Gol',codigo='GO')
  def test_criacao_id(self):
      companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
      self.assertEqual(companhia_1.id, 1)
  def test_update_codigo(self):
      companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
      companhia_1.codigo = 'GL'
      companhia_1.save()
      self.assertEqual(companhia_1.codigo, 'GL')