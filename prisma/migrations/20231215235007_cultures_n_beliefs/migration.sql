-- CreateTable
CREATE TABLE `Culture` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NOT NULL,
    `identity` TEXT NULL,
    `aspects` TEXT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Belief` (
    `id` VARCHAR(191) NOT NULL,
    `name` VARCHAR(191) NOT NULL,
    `description` TEXT NOT NULL,
    `identity` TEXT NULL,
    `aspects` TEXT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `CultureTrait` (
    `id` VARCHAR(191) NOT NULL,
    `culture_id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,
    `conditions` VARCHAR(191) NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `BeliefTrait` (
    `id` VARCHAR(191) NOT NULL,
    `belief_id` VARCHAR(191) NOT NULL,
    `trait_id` VARCHAR(191) NOT NULL,
    `conditions` VARCHAR(191) NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `RaceCulture` (
    `id` VARCHAR(191) NOT NULL,
    `race_id` VARCHAR(191) NOT NULL,
    `culture_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `RaceBelief` (
    `id` VARCHAR(191) NOT NULL,
    `race_id` VARCHAR(191) NOT NULL,
    `belief_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `CultureUnitSpecialization` (
    `id` VARCHAR(191) NOT NULL,
    `unit_specialization_id` VARCHAR(191) NOT NULL,
    `culture_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `BeliefUnitSpecialization` (
    `id` VARCHAR(191) NOT NULL,
    `unit_specialization_id` VARCHAR(191) NOT NULL,
    `belief_id` VARCHAR(191) NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `CultureTrait` ADD CONSTRAINT `CultureTrait_culture_id_fkey` FOREIGN KEY (`culture_id`) REFERENCES `Culture`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CultureTrait` ADD CONSTRAINT `CultureTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `BeliefTrait` ADD CONSTRAINT `BeliefTrait_belief_id_fkey` FOREIGN KEY (`belief_id`) REFERENCES `Belief`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `BeliefTrait` ADD CONSTRAINT `BeliefTrait_trait_id_fkey` FOREIGN KEY (`trait_id`) REFERENCES `Trait`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RaceCulture` ADD CONSTRAINT `RaceCulture_race_id_fkey` FOREIGN KEY (`race_id`) REFERENCES `Race`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RaceCulture` ADD CONSTRAINT `RaceCulture_culture_id_fkey` FOREIGN KEY (`culture_id`) REFERENCES `Culture`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RaceBelief` ADD CONSTRAINT `RaceBelief_race_id_fkey` FOREIGN KEY (`race_id`) REFERENCES `Race`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RaceBelief` ADD CONSTRAINT `RaceBelief_belief_id_fkey` FOREIGN KEY (`belief_id`) REFERENCES `Belief`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CultureUnitSpecialization` ADD CONSTRAINT `CultureUnitSpecialization_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CultureUnitSpecialization` ADD CONSTRAINT `CultureUnitSpecialization_culture_id_fkey` FOREIGN KEY (`culture_id`) REFERENCES `Culture`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `BeliefUnitSpecialization` ADD CONSTRAINT `BeliefUnitSpecialization_unit_specialization_id_fkey` FOREIGN KEY (`unit_specialization_id`) REFERENCES `UnitSpecialization`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `BeliefUnitSpecialization` ADD CONSTRAINT `BeliefUnitSpecialization_belief_id_fkey` FOREIGN KEY (`belief_id`) REFERENCES `Belief`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
