CREATE TABLE `template` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '����',
  `created_at` bigint(11) DEFAULT NULL COMMENT '����ʱ��',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '����ʱ��',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '�Ƿ�ɾ��',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='ģ��';

CREATE TABLE `user` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '����',
  `name` varchar(50) DEFAULT '' COMMENT '�û���',
  `email` varchar(50) DEFAULT 'example@sse.com.cn' COMMENT '����',
  `phone` varchar(11) DEFAULT '' COMMENT '�绰����',
  `password` varchar(50) DEFAULT NULL COMMENT '����',
  `created_at` bigint(11) DEFAULT NULL COMMENT '����ʱ��',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '����ʱ��',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '�Ƿ�ɾ��',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='�û�';
