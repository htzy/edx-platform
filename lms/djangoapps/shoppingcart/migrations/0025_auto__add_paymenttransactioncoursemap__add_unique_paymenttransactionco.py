# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaymentTransactionCourseMap'
        db.create_table('shoppingcart_paymenttransactioncoursemap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shoppingcart.PaymentTransaction'])),
            ('course_id', self.gf('xmodule_django.models.CourseKeyField')(max_length=255, db_index=True)),
            ('order_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shoppingcart.OrderItem'])),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2)),
        ))
        db.send_create_signal('shoppingcart', ['PaymentTransactionCourseMap'])

        # Adding unique constraint on 'PaymentTransactionCourseMap', fields ['transaction', 'course_id', 'order_item']
        db.create_unique('shoppingcart_paymenttransactioncoursemap', ['transaction_id', 'course_id', 'order_item_id'])

        # Adding model 'PaymentTransactionSyncError'
        db.create_table('shoppingcart_paymenttransactionsyncerror', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('remote_transaction_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, db_index=True)),
            ('raw_data', self.gf('django.db.models.fields.TextField')()),
            ('err_msg', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('shoppingcart', ['PaymentTransactionSyncError'])

        # Adding model 'PaymentTransaction'
        db.create_table('shoppingcart_paymenttransaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('remote_transaction_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64, db_index=True)),
            ('account_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('processed_at', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shoppingcart.Order'])),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2)),
            ('transaction_type', self.gf('django.db.models.fields.CharField')(max_length=6, db_index=True)),
        ))
        db.send_create_signal('shoppingcart', ['PaymentTransaction'])

        # Adding model 'PaymentTransactionSync'
        db.create_table('shoppingcart_paymenttransactionsync', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('date_range_start', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('date_range_end', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('rows_processed', self.gf('django.db.models.fields.IntegerField')()),
            ('rows_in_error', self.gf('django.db.models.fields.IntegerField')()),
            ('sync_started_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 14, 0, 0))),
            ('sync_ended_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('shoppingcart', ['PaymentTransactionSync'])


    def backwards(self, orm):
        # Removing unique constraint on 'PaymentTransactionCourseMap', fields ['transaction', 'course_id', 'order_item']
        db.delete_unique('shoppingcart_paymenttransactioncoursemap', ['transaction_id', 'course_id', 'order_item_id'])

        # Deleting model 'PaymentTransactionCourseMap'
        db.delete_table('shoppingcart_paymenttransactioncoursemap')

        # Deleting model 'PaymentTransactionSyncError'
        db.delete_table('shoppingcart_paymenttransactionsyncerror')

        # Deleting model 'PaymentTransaction'
        db.delete_table('shoppingcart_paymenttransaction')

        # Deleting model 'PaymentTransactionSync'
        db.delete_table('shoppingcart_paymenttransactionsync')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shoppingcart.certificateitem': {
            'Meta': {'object_name': 'CertificateItem', '_ormbases': ['shoppingcart.OrderItem']},
            'course_enrollment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student.CourseEnrollment']"}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '128', 'db_index': 'True'}),
            'mode': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'orderitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shoppingcart.OrderItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'shoppingcart.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 14, 0, 0)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'percentage_discount': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'shoppingcart.couponredemption': {
            'Meta': {'object_name': 'CouponRedemption'},
            'coupon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.Coupon']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.Order']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'shoppingcart.courseregcodeitem': {
            'Meta': {'object_name': 'CourseRegCodeItem', '_ormbases': ['shoppingcart.OrderItem']},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '128', 'db_index': 'True'}),
            'mode': ('django.db.models.fields.SlugField', [], {'default': "'honor'", 'max_length': '50'}),
            'orderitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shoppingcart.OrderItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'shoppingcart.courseregcodeitemannotation': {
            'Meta': {'object_name': 'CourseRegCodeItemAnnotation'},
            'annotation': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shoppingcart.courseregistrationcode': {
            'Meta': {'object_name': 'CourseRegistrationCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 14, 0, 0)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_by_user'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.Invoice']", 'null': 'True'}),
            'mode_slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchase_order'", 'null': 'True', 'to': "orm['shoppingcart.Order']"})
        },
        'shoppingcart.donation': {
            'Meta': {'object_name': 'Donation', '_ormbases': ['shoppingcart.OrderItem']},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'donation_type': ('django.db.models.fields.CharField', [], {'default': "'general'", 'max_length': '32'}),
            'orderitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shoppingcart.OrderItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'shoppingcart.donationconfiguration': {
            'Meta': {'object_name': 'DonationConfiguration'},
            'change_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.PROTECT'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shoppingcart.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'company_contact_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'customer_reference_number': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recipient_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipient_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'total_amount': ('django.db.models.fields.FloatField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        'shoppingcart.order': {
            'Meta': {'object_name': 'Order'},
            'bill_to_cardtype': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'bill_to_ccnum': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'bill_to_city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'bill_to_country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'bill_to_first': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'bill_to_last': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'bill_to_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'bill_to_state': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'bill_to_street1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'bill_to_street2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'company_contact_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company_contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'usd'", 'max_length': '8'}),
            'customer_reference_number': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_type': ('django.db.models.fields.CharField', [], {'default': "'personal'", 'max_length': '32'}),
            'processor_reply_dump': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'purchase_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recipient_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'refunded_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'cart'", 'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'shoppingcart.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'usd'", 'max_length': '8'}),
            'fulfilled_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_desc': ('django.db.models.fields.CharField', [], {'default': "'Misc. Item'", 'max_length': '1024'}),
            'list_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '30', 'decimal_places': '2'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.Order']"}),
            'qty': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'refund_requested_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'report_comments': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'service_fee': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '30', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'cart'", 'max_length': '32', 'db_index': 'True'}),
            'unit_cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '30', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'shoppingcart.paidcourseregistration': {
            'Meta': {'object_name': 'PaidCourseRegistration', '_ormbases': ['shoppingcart.OrderItem']},
            'course_enrollment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student.CourseEnrollment']", 'null': 'True'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '128', 'db_index': 'True'}),
            'mode': ('django.db.models.fields.SlugField', [], {'default': "'honor'", 'max_length': '50'}),
            'orderitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shoppingcart.OrderItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'shoppingcart.paidcourseregistrationannotation': {
            'Meta': {'object_name': 'PaidCourseRegistrationAnnotation'},
            'annotation': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shoppingcart.paymenttransaction': {
            'Meta': {'object_name': 'PaymentTransaction'},
            'account_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.Order']"}),
            'processed_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'remote_transaction_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_index': 'True'})
        },
        'shoppingcart.paymenttransactioncoursemap': {
            'Meta': {'unique_together': "(('transaction', 'course_id', 'order_item'),)", 'object_name': 'PaymentTransactionCourseMap'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '2'}),
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.OrderItem']"}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.PaymentTransaction']"})
        },
        'shoppingcart.paymenttransactionsync': {
            'Meta': {'object_name': 'PaymentTransactionSync'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_range_end': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'date_range_start': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'rows_in_error': ('django.db.models.fields.IntegerField', [], {}),
            'rows_processed': ('django.db.models.fields.IntegerField', [], {}),
            'sync_ended_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'sync_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 14, 0, 0)'})
        },
        'shoppingcart.paymenttransactionsyncerror': {
            'Meta': {'object_name': 'PaymentTransactionSyncError'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'err_msg': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'raw_data': ('django.db.models.fields.TextField', [], {}),
            'remote_transaction_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'})
        },
        'shoppingcart.registrationcoderedemption': {
            'Meta': {'object_name': 'RegistrationCodeRedemption'},
            'course_enrollment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student.CourseEnrollment']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.Order']", 'null': 'True'}),
            'redeemed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 14, 0, 0)', 'null': 'True'}),
            'redeemed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'registration_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shoppingcart.CourseRegistrationCode']"})
        },
        'student.courseenrollment': {
            'Meta': {'ordering': "('user', 'course_id')", 'unique_together': "(('user', 'course_id'),)", 'object_name': 'CourseEnrollment'},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'honor'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['shoppingcart']