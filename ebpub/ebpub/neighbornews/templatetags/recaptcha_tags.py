#   Copyright 2011 OpenPlans and contributors
#
#   This file is part of ebpub
#
#   ebpub is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   ebpub is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with ebpub.  If not, see <http://www.gnu.org/licenses/>.
#

from django import template  
from django.conf import settings  
from recaptcha.client import captcha

register = template.Library()

@register.simple_tag
def recaptcha_html():
    if not getattr(settings, 'RECAPTCHA_PUBLIC_KEY', None):
        return ''
    html = u"<script>var RecaptchaOptions = {theme : 'white'};</script>"
    html += captcha.displayhtml(settings.RECAPTCHA_PUBLIC_KEY)
    return html
