odoo.define('hh_manage_candidate.WidgetCustom', function (require) {
    "use strict";
    var core = require('web.core');
    var session = require('web.session');
    var common = require('web.form_common');
    var QWeb = core.qweb;
    var list_widget_registry = core.list_widget_registry;
    var _t = core._t;
    var pyeval = require('web.pyeval');


    var FieldBooleanButton = common.AbstractField.extend({
        events: {
            'click': function() {
                this.internal_set_value(!this.get('value'));
                this.render_value();
            }
        },
        start: function() {
            this.$checkbox = this.$('input');

            this.$checkbox.prop('disabled', this.get("effective_readonly"));
            this.on("change:effective_readonly", this, function() {
                this.$checkbox.prop('disabled', this.get("effective_readonly"));
            });

            this.string_true = this.options["terminology"];

            this.setupFocus(this.$checkbox);

            return this._super();
        },
        render_value: function() {
//            this.$checkbox.prop('checked', this.get('value'));
            this.$el.html(QWeb.render("MyBoolColor", {widget: this}));
        },
        focus: function() {
            return this.$checkbox.focus();
        },
        set_dimensions: function(height, width) {}, // Checkboxes have a fixed height and width (even in list editable)
        is_false: function() {
            return false;
        },
//        render_value: function() {
//            this._super();
//
//        },
//        is_false: function() {
//            return false;
//        },
    });

    core.form_widget_registry.add('bool_color', FieldBooleanButton);
});