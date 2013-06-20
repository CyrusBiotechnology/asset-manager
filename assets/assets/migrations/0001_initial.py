# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Asset'
        db.create_table(u'assets_asset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acquisition_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('acquisition_value', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.Location'])),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('asset_status', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('charge_type', self.gf('django.db.models.fields.CharField')(default='expense', max_length=100, blank=True)),
            ('make', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.AssetMake'])),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.AssetModel'])),
            ('invoices', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'assets', ['Asset'])

        # Adding model 'AssetMake'
        db.create_table(u'assets_assetmake', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'assets', ['AssetMake'])

        # Adding model 'AssetModel'
        db.create_table(u'assets_assetmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.AssetMake'])),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('model_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assets.AssetType'], null=True, blank=True)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('manual', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('drivers', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'assets', ['AssetModel'])

        # Adding model 'AssetCheckout'
        db.create_table(u'assets_assetcheckout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='', to=orm['auth.User'])),
            ('asset', self.gf('django.db.models.fields.related.ForeignKey')(related_name='', to=orm['assets.Asset'])),
            ('out_date', self.gf('django.db.models.fields.DateField')()),
            ('in_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'assets', ['AssetCheckout'])

        # Adding model 'Location'
        db.create_table(u'assets_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_state', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal(u'assets', ['Location'])

        # Adding model 'AssetType'
        db.create_table(u'assets_assettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal(u'assets', ['AssetType'])

        # Adding model 'ImportFile'
        db.create_table(u'assets_importfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uploaded', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'assets', ['ImportFile'])


    def backwards(self, orm):
        # Deleting model 'Asset'
        db.delete_table(u'assets_asset')

        # Deleting model 'AssetMake'
        db.delete_table(u'assets_assetmake')

        # Deleting model 'AssetModel'
        db.delete_table(u'assets_assetmodel')

        # Deleting model 'AssetCheckout'
        db.delete_table(u'assets_assetcheckout')

        # Deleting model 'Location'
        db.delete_table(u'assets_location')

        # Deleting model 'AssetType'
        db.delete_table(u'assets_assettype')

        # Deleting model 'ImportFile'
        db.delete_table(u'assets_importfile')


    models = {
        u'assets.asset': {
            'Meta': {'object_name': 'Asset'},
            'acquisition_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'acquisition_value': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'asset_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.Location']"}),
            'asset_status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'charge_type': ('django.db.models.fields.CharField', [], {'default': "'expense'", 'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoices': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.AssetMake']"}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.AssetModel']"}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'assets.assetcheckout': {
            'Meta': {'object_name': 'AssetCheckout'},
            'asset': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "''", 'to': u"orm['assets.Asset']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'out_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "''", 'to': u"orm['auth.User']"})
        },
        u'assets.assetmake': {
            'Meta': {'object_name': 'AssetMake'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'assets.assetmodel': {
            'Meta': {'object_name': 'AssetModel'},
            'drivers': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.AssetMake']"}),
            'manual': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'model_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.AssetType']", 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'assets.assettype': {
            'Meta': {'object_name': 'AssetType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'assets.importfile': {
            'Meta': {'object_name': 'ImportFile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploaded': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'assets.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_state': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['assets']