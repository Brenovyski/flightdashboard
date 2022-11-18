from django.test import TestCase

from sys_voos.models import CompanhiaAerea, Voo, Partida, Chegada

import datetime
from django.utils import timezone

class CompanhiaAereaTest(TestCase):
  @classmethod
  def setUpTestData(cls):
      CompanhiaAerea.objects.create(nome='Gol',codigo='GO')
      CompanhiaAerea.objects.create(nome='Latam')
  def test_companhia_id_1(self):
      companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
      self.assertEqual(companhia_1.id, 1)
  def test_companhia_id_1(self):
      companhia_2 = CompanhiaAerea.objects.get(nome='Latam')
      self.assertEqual(companhia_2.id, 2)
  def test_companhia_codigo_1(self):
      #https://stackoverflow.com/questions/51148893/object-created-even-if-field-was-required
      companhia_2 = CompanhiaAerea.objects.get(nome='Latam')
      self.assertEqual(companhia_2.codigo, '')
  def test_update_codigo(self):
      companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
      companhia_1.codigo = 'GL'
      companhia_1.save()
      self.assertEqual(companhia_1.codigo, 'GL')

class VooModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    CompanhiaAerea.objects.create(nome='Gol')
    companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
    horario = datetime.time(10,30) #10 horas e 30 min
    Voo.objects.create(companhia=companhia_1, horario_previsto=horario, local='Argentina', codigo='GL3249')

  def test_voo_codigo(self):
    companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
    voo_1 = Voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.codigo, 'GL3249')

  def test_voo_id(self):
    companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
    voo_1 = Voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.id, 1)

  def test_horario_previsto(self):
    companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
    voo_1 = Voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.horario_previsto, datetime.time(10,30))

  def test_local(self):
    companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
    voo_1 = Voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.local, 'Argentina')

class PartidaModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    CompanhiaAerea.objects.create(nome='Gol')
    companhia_1 = CompanhiaAerea.objects.get(nome='Gol')
    horario = datetime.time(10,30) #10 horas e 30 min
    Voo.objects.create(companhia=companhia_1, horario_previsto=horario, local='Argentina')
    voo_1 = Voo.objects.get(companhia=companhia_1)
    dia = datetime.date(2022, 10, 2)
    Partida.objects.create(voo=voo_1, data=dia)

  def test_partida_id(self):
    voo_1 = Voo.objects.get(id=1)
    partida_1 = Partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.id, 1)

  def test_partida_data(self):
    voo_1 = Voo.objects.get(id=1)
    partida_1 = Partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.data, datetime.date(2022, 10, 2))

  def test_partida_status(self):
    voo_1 = Voo.objects.get(id=1)
    partida_1 = Partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.status, 'EM')

  def test_partida_horario_real(self):
    voo_1 = Voo.objects.get(id=1)
    partida_1 = Partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.horario_real, None)
  
class ChegadaModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    CompanhiaAerea.objects.create(nome='Latam')
    companhia_1 = CompanhiaAerea.objects.get(nome='Latam')
    horario = datetime.time(10,30) #10 horas e 30 min
    Voo.objects.create(companhia=companhia_1, horario_previsto=horario, local='Argentina')
    voo_1 = Voo.objects.get(companhia=companhia_1)
    dia = datetime.date(2022, 11, 21)
    Chegada.objects.create(voo=voo_1, data=dia)

  def test_chegada_id(self):
    voo_1 = Voo.objects.get(id=1)
    chegada_1 = Chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.id, 1)

  def test_chegada_data(self):
    voo_1 = Voo.objects.get(id=1)
    chegada_1 = Chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.data, datetime.date(2022, 11, 21))

  def test_chegada_status(self):
    voo_1 = Voo.objects.get(id=1)
    chegada_1 = Chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.status, 'VO')

  def test_chegada_horario_real(self):
    voo_1 = Voo.objects.get(id=1)
    chegada_1 = Chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.horario_real, None)
  
